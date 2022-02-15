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
        bat 'pyinstaller --onefile app.py'
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
    stage('Configure Artifactory'){
      steps{
        script {
          
          echo '********* Configure Artifactory Started **********'
             def userInput = input(
             id: 'userInput', message: 'Enter password for Artifactory', parameters: [
             
             [$class: 'TextParameterDefinition', defaultValue: 'password', description: 'Artifactory Password', name: 'password']])
             
             bat 'jfrog rt c artifactory-demo --url=http://34.68.191.118:8081/artifactory --user=admin --password='+userInput
             
          echo '********* Configure Artifactory Finished **********'
        }
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
            archiveArtifacts artifacts: 'dist/*.exe', fingerprint: true
            junit 'test-reports/*.xml'
          script{
            if(currentBuild.currentResult=='SUCCESS')
            {
              echo '********* Uploading to Artifactory is Started **********'
              /*bat 'jfrog rt u "dist/*.exe" generic-local'*/
              bat 'Powershell.exe -executionpolicy remotesigned -File build_script.ps1'
              echo '********* Uploading Finished **********'
            }
          }
          
            
            deleteDir()

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
