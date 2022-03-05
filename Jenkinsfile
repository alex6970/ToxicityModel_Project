pipeline {
agent any
environment {
    PATH = "$PATH:/usr/local/bin"
}


stages {

stage('Test git') {
            steps {
                sh 'git status'

            }
        }

stage('Building') {
      steps {

        sh 'docker-compose build'

            }
          }

stage('Running the container') {
      steps {

        sh 'docker-compose up -d'

            }
          }

  stage('Container down and cleaning') {
        steps {

          sh 'docker-compose down'

              }
            }

  }
}
