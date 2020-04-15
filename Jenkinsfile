pipeline {
  agent any
  stages {
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        bat 'pip install -r requirements.txt'
        echo '********* Build Stage Finished **********'
        }
    }
    stage('Testing Stage') {
      steps {
        echo '********* Test Stage Started **********'
        bat 'python test.py'
        echo '********* Test Stage Finished **********'
      }   
    }
    stage('Sanity check') {
            steps {
                input "Does the staging environment look ok?"
            }
     }
stage('Deployment Stage'){
            steps{
                input "Do you want to Deploy the application?"
                echo '********* Deploy Stage Started **********'
                timeout(time : 1, unit : 'MINUTES')
                {
                bat 'python app.py'
                }
                echo '********* Deploy Stage Finished **********'
            }
    }
  }
  post {
        always {
            echo 'We came to an end!'
         }
        success {
          echo 'Build Successfull!!'
    }
        failure {
        echo 'Sorry mate! build is Failed :('
    }
        unstable {
            echo 'Run was marked as unstable'
        }
        changed {
            echo 'Hey look at this, Pipeline state is changed.'
        }
    }
}
