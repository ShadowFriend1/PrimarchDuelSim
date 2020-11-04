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
    }
}
