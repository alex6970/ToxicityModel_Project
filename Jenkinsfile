pipeline {
agent any
environment {
    PATH = "$PATH:/usr/local/bin"
}


stages {

  stage('Building') {
        steps {


  stage('Running the test') {
        steps {

          sh 'cd tests'
          sh 'pip3 install -r requirements.txt'
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
