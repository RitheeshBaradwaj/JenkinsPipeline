pipeline {
  agent any
  stages {
    stage('Clean Reports')
    {
      steps{
        echo '********* Cleaning Workspace Stage Started **********'
        bat 'rmdir /s /q test-reports'
        echo '********* Cleaning Workspace Stage Finished **********'
      }
    }
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        bat 'pip install -r requirements.txt'
        bat 'jfrog rt c artifactory-demo --url=http://34.68.191.118:8081/artifactory --user=admin --password=rit4@1999'
        bat 'jfrog rt pip-install -r requirements.txt --build-name=my-build --build-number=1'
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
            archiveArtifacts artifacts: 'test-reports/*.xml', fingerprint: true
            junit 'test-reports/*.xml'
            bat 'jfrog rt u "test-reports/*.xml" generic-local'

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
