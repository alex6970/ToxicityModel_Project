pipeline {
agent any

stages {

  stage('Building') {
        steps {

          sh '/usr/local/bin/docker_compose build'

              }
            }

  stage('Running the container') {
        steps {

          sh '/usr/local/bin/docker_compose up -d'

              }
            }

  stage('Running the test') {
        steps {

          sh 'cd tests'
          sh 'python -m pytest'

              }
            }

  stage('Container down and cleaning') {
        steps {

          sh 'docker-compose down'

              }
            }

  }
}
