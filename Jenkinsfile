pipeline {
    environment {
        registry = "yosale/wog-score"
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
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build registry
                }
            }
        }
        stage('Run') {
            steps {
                sh "docker-compose up --d"
            }
        }
        stage('Test') {
            steps {
                sh "ls -ltr"
            }
        }
        stage('Finalize') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
                sh "docker rmi $registry"
            }
        }
    }
}