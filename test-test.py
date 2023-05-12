pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Augustin47/flaskcourses.git']]])
            }
        }
        stage('Install dependencies') {
            steps {
                git branch: 'main', url: 'https://github.com/Augustin47/flaskcourses.git'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Install corverage') {
            steps {
                sh 'pip3 install coverage'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 -m coverage run --source=./ -m pytest'
                sh 'python3 -m coverage xml'
            }
        }

        stage('SonarQube analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube Scanner';
                    withSonarQubeEnv() {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=flaskcourses"
                    }
                }
            }
        }
        stage('Create artifact') {
            steps {
                sh 'zip -r my_artifact.zip .'
            }
        }
        stage('Archive artifact') {
            steps {
                archiveArtifacts artifacts: 'my_artifact.zip', fingerprint: true
            }
        }
    }
}
