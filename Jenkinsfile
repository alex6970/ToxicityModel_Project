pipeline {
agent any
environment {
    PATH = "$PATH:/usr/local/bin"
}


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

          sh 'cd tests'
          sh 'python -m pip install --upgrade pip'
          sh 'pip install -r requirements.txt'
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
