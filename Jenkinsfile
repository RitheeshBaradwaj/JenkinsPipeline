pipeline {
  agent { docker { image 'python:3.7-slim' } }
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
    stage('Sanity check') {
            steps {
                input "Does the staging environment look ok?"
            }
     }
stage('Deployment Stage'){
            steps{
                input "Do you want to Deploy the application?"
                echo '********* Deploy Stage Started **********'
                sh 'python app.py'
                echo '********* Deploy Stage Finished **********'
            }
    }
  }
  post {
        always {
            echo 'We came to an end!'
            deleteDir() /* clean up our workspace */
        }
        success {
        mail to: 'bunnyrb4@gmail.com',
             subject: "The pipeline ${currentBuild.fullDisplayName} completed successfully.",
             body: "Everything is working normally"
    }
        failure {
        mail to: 'bunnyrb4@gmail.com',
             subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             body: "Something is wrong with ${env.BUILD_URL}"
    }
        unstable {
            echo 'Run was marked as unstable'
        }
        changed {
            echo 'Hey look at this, Pipeline state is changed.'
        }
    }
}
