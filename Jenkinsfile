pipeline {
  agent {
    label 'master'
    }
  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t dad-jokes-chatbot .'
      }
    }
    stage('Run Container') {
      steps {
        sh 'docker run -d -p 5000:5000 dad-jokes-chatbot'
        sh 'echo "Running on http://127.0.0.1:5000"'
      }
    }
  }
}
