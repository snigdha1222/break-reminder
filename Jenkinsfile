pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "snigdha1222/break-reminder"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'jenkins-push',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag ${DOCKER_IMAGE}:latest ${DOCKER_IMAGE}:v1
                        docker push ${DOCKER_IMAGE}:latest
                        docker push ${DOCKER_IMAGE}:v1
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '🎉 Image pushed successfully to Docker Hub!'
        }
        failure {
            echo '❌ Something went wrong during the pipeline.'
        }
    }
}
