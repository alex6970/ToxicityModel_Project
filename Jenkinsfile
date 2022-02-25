pipeline {
agent any
    stages {
        stage('Build and Running') {
            steps {
                bat 'docker-compose up'
                // echo 'It works'
            }
        }

        stage('Running tests') {
                    steps {

                  // add steps to run python tests
                  // cf. jenkins branch selection

                  bat 'cd tests'
                  bat 'python -m pytest'
            }
        }

        stage('Shutting down') {
                    steps {

                    bat 'docker-compose down'

            }
        }
    }
}
