pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        sh 'pip install -r requirements.txt'
        echo '********* Build Stage Finished **********'
        }
    }
    stage('Testing Stage') {
      steps {
        echo '********* Test Stage Started **********'
        sh 'python test.py'
        echo '********* Test Stage Finished **********'
      }   
    }
    if(currentBuild.currentResult == 'SUCCESS')
    {
        stage('Deployment Stage'){
            steps{
                input "Do you want to Deploy the application?"
                echo '********* Deploy Stage Started **********'
                sh 'python app.py'
                echo '********* Deploy Stage Finished **********'
            }
        }
    }
  }
  post {
        always {
            echo 'We came to an end!'
        }
        success {
            echo 'Build is Successfull !'
        }
        failure {
            echo 'Sorry mate! Build is Failed! :('
        }
        unstable {
            echo 'Run was marked as unstable'
        }
        changed {
            echo 'Hey look at this, Pipeline state is changed.'
        }
    }
}
