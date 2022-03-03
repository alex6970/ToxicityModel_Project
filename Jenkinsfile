pipeline {
agent any

stages {

  stage('Building') {
        steps {

          bat 'docker-compose build'

              }
            }

  stage('Running the container') {
        steps {

          bat 'docker-compose up -d'

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
