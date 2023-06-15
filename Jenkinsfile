pipeline {
   // Agent block
   agent any

   // Stage Block
   stages {// stage blocks
      stage("Build docker images") {
         steps {
            script {
               echo "Building docker images"
               def buildArgs = """\ --build-arg HTTP_PROXY=${params.HTTP_PROXY} \ --build-arg HTTPS_PROXY=${params.HTTPS_PROXY} \ -f Dockerfile \ ."""
                docker.build(
                   "${params.Image_Name}:${params.Image_Tag}",
                   buildArgs)
            }
         }
      }
   }
}