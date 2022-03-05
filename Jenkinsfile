pipeline {
agent any
environment {
    PATH = "$PATH:/usr/local/bin"
}


stages {



  stage('Running the test') {
        steps {

          sh 'cd tests'
          sh 'pip3.9 install -r requirements.txt'
          sh 'python3.9 -m pytest'

              }
            }

  stage('Container down and cleaning') {
        steps {

          sh 'docker-compose down'

              }
            }

  }
}
