pipeline {
agent any


stages {

stage('Feature branch deployment, testing') {
  when {
                branch 'feature_branch'
            }

      steps {
        bat 'echo Hello'
        //bat '''
        //echo feature-branch
        //docker-compose build
        //docker-compose up -d

        //cd tests
        //python -m pytest
        // '''

            }
  }


  stage('Feature branch push to develop') {
    when {
                  branch 'feature_branch'
              }

        steps {
        bat 'echo GIT_BRANCH'
        bat '''
        git fetch
        git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
        git checkout ${GIT_BRANCH}
        git branch
        '''


              }
    }

  stage('Git testing release') {

        steps {

          bat 'git branch'

              }
            }


  stage('Git develop') {
    when {
                  branch 'develop'
              }

        steps {

          bat 'echo develop'

              }
            }

  stage('Git master') {
    when {
                  branch 'master'
              }

        steps {

          bat 'echo master'

              }
            }



  }
}
