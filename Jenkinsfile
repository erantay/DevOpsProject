pipeline {
    environment {
        registry = "https://hub.docker.com"
        registryCredential = 'dockerhub-account'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/erantay/DevOpsProject.git'
            }
        }
        stage('Building our image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}