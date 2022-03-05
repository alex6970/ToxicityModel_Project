pipeline {
agent any
environment {
    PATH = "$PATH:/usr/local/bin"
}


stages {

  stage('Building') {
        steps {

          sh 'echo $PATH'

          // sh 'export PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/local/bin/'

          sh '/usr/local/bin/docker-compose build'

              }
            }

  stage('Running the container') {
        steps {

          sh 'docker-compose up -d'

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
