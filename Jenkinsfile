pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Am1t-levy/Meme_Generator.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t meme_generator .'

                    echo 'Building the project completed'
                }
            }
        }
        stage('Deploy') {
            steps {
                // Deploy Docker container
                sh 'docker run -d -p 5000:5000 meme_generator'

                echo 'Deploying the project'
            }
        }
    }
}

