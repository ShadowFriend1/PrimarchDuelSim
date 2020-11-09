pipeline {
    agent any
    stages {
		stage('SonarQube analysis') {
			environment {
        		scannerHome = tool 'SonarQubeScanner'
    		}    
			steps {
        		withSonarQubeEnv('My SonarQube Server') {
            		sh "${scannerHome}/bin/sonar-scanner"
				}
        	}
		}
		stage('Checkout Git Comment Program') {
			steps {
				git credentialsId: '33be1895-4822-4709-9977-56ae072efd6f', url: 'https://github.com/ShadowFriend1/pr-Decoration.git'
			}
		}
		stage('Post Pull Request Comment') {
			environment {
				goInstallation = tool 'Go:latest'
				withSonarQubeEnv('My SonarQube Server') {
            		SONARQUBEURL = env.SONAR_HOST_URL
				}
				SONARQUBEPROJECT = my:project
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'my-sonarqube-server-login',
								usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
					SONARQUBEUSER = USERNAME
					SONARQUBEPASSWORD = PASSWORD
 				}
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aab572d0-f1d3-4f9b-b930-812bcb49d485',
								usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
					GITHUB_API_KEY = PASSWORD
 				}
			}
			steps {
				withEnv(["GOROOT=${Go:latest}", "PATH+GO=${Go:latest}/bin"]) {
					sh 'go run new.go'
				}
			}
		}
    }
}
