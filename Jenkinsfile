pipeline {
agent any
environment {
    PATH = "$PATH:/usr/local/bin"
}


stages {



  stage('Running the test') {
        steps {

          sh 'cd tests'
          sh 'pip3 install -U pytest'
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
