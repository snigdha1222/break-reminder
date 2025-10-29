pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "snigdha1222/break-reminder"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning repository from GitHub...'
                git branch: 'main', url: 'https://github.com/snigdha1222/break-reminder.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Run Container for Testing') {
            steps {
                echo 'Running temporary container for testing...'
                sh 'docker run -d -p 5000:5000 --name break-test $DOCKER_IMAGE:latest'
                sh 'sleep 5'
                sh 'curl http://localhost:5000/health || echo "Health check failed!"'
                sh 'docker stop break-test && docker rm break-test'
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                echo 'Pushing image to DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker tag $DOCKER_IMAGE:latest $DOCKER_IMAGE:1
                    docker push $DOCKER_IMAGE:latest
                    docker push $DOCKER_IMAGE:1
                    docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying application to Kubernetes...'
                sh '''
                kubectl apply -f k8s-deployment.yaml
                kubectl apply -f k8s-service.yaml
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build and deployment successful!'
        }
        failure {
            echo '❌ Build failed. Check console output for details.'
        }
    }
}
