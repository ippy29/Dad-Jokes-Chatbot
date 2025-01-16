pipeline {
  agent {
    label 'Build02'
    }
  stages {
    stage('Build Docker Image') {
      steps {
        // script {
        //   docker.build("dad-jokes-chatbot", "-f Dockerfile .")
        // }
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
  // cleanup
  // post {
  //   always {
  //     script{
  //       sh 'docker rm $(docker stop $(docker ps -q --filter "ancestor=dad-jokes-chatbot"))' // stops then removes container
  //     }
  //   }
  // }
}