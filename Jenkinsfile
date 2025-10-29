pipeline {
  agent any
  environment {
    DOCKERHUB_CRED = 'dockerhub-creds'
    DOCKERHUB_REPO = 'yourdockerhubusername/break-reminder'
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build Image') {
      steps {
        sh "docker build -t ${DOCKERHUB_REPO}:${BUILD_NUMBER} ."
        sh "docker tag ${DOCKERHUB_REPO}:${BUILD_NUMBER} ${DOCKERHUB_REPO}:latest"
      }
    }
    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CRED}", usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh "echo $PASS | docker login -u $USER --password-stdin"
          sh "docker push ${DOCKERHUB_REPO}:${BUILD_NUMBER}"
          sh "docker push ${DOCKERHUB_REPO}:latest"
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        sh "kubectl apply -f k8s-deployment.yaml"
        sh "kubectl apply -f k8s-service.yaml"
      }
    }
  }
}
