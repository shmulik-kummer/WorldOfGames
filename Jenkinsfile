pipeline {
    agent any

    stages {
        // checks out the 'master' branch
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'master']],
                    userRemoteConfigs: [[url: 'https://github.com/shmulik-kummer/WorldOfGames.git']]
                ])
            }
        
        // Build the docker image
        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }
        // Run a container. exposing port 8777 and binding the Scores.txt file.
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5000 -v $(pwd)/Scores.txt:/app/Scores.txt myapp'
            }
        }
        // wraps the execution of the 'e2e.py' test script with an Xvfb virtual frame buffer to enable headless execution.
        stage('Test') {
            steps {
                wrap([$class: 'Xvfb']) {
                sh 'python3 tests/e2e.py'
        }
    }
        }
        
        stage('Finalize') {
            steps {
                // Stop the running container
                sh 'docker stop $(docker ps -q --filter ancestor=myapp)'
                // Tag the image (prepare for push)
                sh 'docker tag myapp kummer/myapp'
                script {
                    // Push the image to dockerhub (using credentials stored on jenkins)
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                        sh 'docker push kummer/myapp'
                    }
                }}
        }
    }
}
}