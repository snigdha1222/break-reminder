pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "Snigdha1222/break-reminder"
        DOCKER_TAG = "latest"
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
                    echo "🔨 Building Docker image..."
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                script {
                    echo "📦 Pushing Docker image to Docker Hub..."
                    withCredentials([usernamePassword(
                        credentialsId: 'jenkins-push',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                            docker logout
                        '''
                    }
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
