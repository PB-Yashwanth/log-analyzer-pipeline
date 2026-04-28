pipeline {
    agent any

    triggers {
        pollSCM('* * * * *') // runs every minute (for demo)
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/PB-Yashwanth/log-analyzer-pipeline.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 analyzer.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
