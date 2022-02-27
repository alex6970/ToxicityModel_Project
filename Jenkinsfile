pipeline {
agent any
if(env.BRANCH_NAME == 'develop'){

stages {
    stage('Build and Running') {
        steps {
            bat 'docker-compose up -d --build'
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
}
