pipeline {
agent any
    stages {
        stage('Build and Running') {
            when {
                    branch 'develop'
                }
            steps {
                bat 'docker-compose up -d --build'
                // echo 'It works'
            }
        }

        stage('Running tests') {
              when {
                      branch 'develop'
                  }
                    steps {

                  // add steps to run python tests
                  // cf. jenkins branch selection

                  bat 'cd tests'
                  bat 'python -m pytest'
            }
        }

        stage('Shutting down') {
            when {
                    branch 'develop'
                }
                    steps {

                    bat 'docker-compose down'

            }
        }
    }
}
