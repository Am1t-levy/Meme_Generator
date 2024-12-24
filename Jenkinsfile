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
                script {
                    // Deploy Docker container
                    sh 'docker run -d -p 5000:5000 --name meme_generator meme_generator'
                    echo 'Deploying the project'
                    
                    // Wait for the container to be ready
                    sh '''
                    while ! curl -s http://localhost:5000; do
                        echo "Waiting for app to start..."
                        sleep 5
                    done
                    '''
                }
            }
        }
    }
}


