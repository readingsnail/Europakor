chcp 65001
java -Dfile.encoding=UTF-8 -cp lib/* org.zanata.client.ZanataClient  push --user-config zanata.ini --project-config Batch.xml --push-type source -s SOURCE
