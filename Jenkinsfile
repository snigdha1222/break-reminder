pipeline {
    agent any
    stages {
        stage("Build Docker image") {
            steps {
                echo "Build Docker image"
                bat "docker build -t break-reminder:v1 ."
            }
        }
        stage("Docker Login") {
            steps {
                bat "docker login -u snigdha1222 -p Snigdha@08"
            }
        }
        stage("push Docker image to docker hub") {
            steps {
                echo "push Docker image to docker hub"
                bat "docker tag break-reminder:v1 snigdha1222/break-reminder:t8"
                bat "docker push snigdha1222/break-reminder:t8"
            }
        }
        stage("Deploy to kubernetes") {
            steps {
                echo "Deploy to kubernetes"
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }
    post {
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "pipeline failed. Please check the logs"
        }
    }
}
