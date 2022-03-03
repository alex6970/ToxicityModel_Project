pipeline {
agent any

stages {

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

  stage('Running the test') {
        steps {

          bat 'cd tests'
          bat 'python -m pytest'

              }
            }

  stage('Container down and cleaning') {
        steps {

          bat 'docker-compose down'

              }
            }

  }
}
