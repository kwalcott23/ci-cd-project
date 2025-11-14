// Jenkinsfile

pipeline {
    agent any

    environment {
        // ID of the WebEx Bot Token credential created in Jenkins
        WEBEX_TOKEN_CREDENTIAL_ID = 'MmIyZDhhYTctMWY5Yy00NGFlLThlNDUtNjY3NWZjYTRkMTUwNDcwNTY3MjQtMjk1_P0A1_13494cac-24b4-4f89-8247-193cc92a7636' 
        WEBEX_ROOM_ID = 'ffe73670-c12c-11f0-a111-3dfd2b65a66c' // Replace with your WebEx Space ID
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                // Code is automatically checked out by the Pipeline SCM configuration
            }
        }

        stage('Build & Test') {
            steps {
                echo 'Installing dependencies and running tests...'
                // Assuming a standard Linux-based agent (Docker container usually works fine)
                sh 'pip install unittest'
                sh 'python -m unittest tests/test_main.py'
            }
        }
    }

    post {
        // Always attempt to send a notification after the build is complete
        always {
            // Determine the build status
            script {
                def buildStatus = currentBuild.result ?: 'SUCCESS'
                def webexMessage
                
                if (buildStatus == 'SUCCESS') {
                    webexMessage = "✅ **BUILD SUCCESSFUL** for job: ${env.JOB_NAME} [Build #${env.BUILD_NUMBER}] - Git Commit: ${env.GIT_COMMIT.substring(0, 7)} - View details: ${env.BUILD_URL}"
                } else if (buildStatus == 'FAILURE') {
                    webexMessage = "❌ **BUILD FAILED** for job: ${env.JOB_NAME} [Build #${env.BUILD_NUMBER}] - Git Commit: ${env.GIT_COMMIT.substring(0, 7)} - View details: ${env.BUILD_URL}"
                } else {
                    webexMessage = "⚠️ **BUILD STATUS: ${buildStatus}** for job: ${env.JOB_NAME} - View details: ${env.BUILD_URL}"
                }
                
                // Use the installed WebEx Notifier plugin function 
                // NOTE: The exact syntax might vary slightly depending on the specific WebEx plugin installed.
                // This is a common pattern for Jenkins notification plugins.
                webEx.send(
                    roomId: "${env.WEBEX_ROOM_ID}",
                    tokenCredentialId: "${env.WEBEX_TOKEN_CREDENTIAL_ID}",
                    message: webexMessage
                )
            }
        }
    }
}
