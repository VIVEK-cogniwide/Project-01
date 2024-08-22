#Given Requirements & Sequence Flow 
Requirement

•              Create 2 VPC/Vnet (network-a & network-b)

•              Create 2 subnets in each VPC (network-a -> subnet-a & subnet-b ; network-b -> subnet-c & subnet-d)

•              Create 1 VM (vm-nginx) as public in subnet-a and 1 VM (vm-connect) as private in subnet-b; both belongs to network-a

•              Create 2 VM (vm-app-1 & vm-app-2) as private in subnet-c in network-b

•              Deploy an Nginx proxy server in vm-nginx (network-a -> subnet-a)

•              Nginx should be accessible from the internet and only from the user's browser. It should restrict traffic from the rest of the internet.

•              Develop on your own and deploy a sample CRUD REST API in Python or Golang.

•              Deploy the sample API in vm-app-1 & vm-app-2

•              Create an internet-facing NLB for the sample API hosted in both vm-app-1 & vm-app-2

•              The sample API should be accessible publicly via the loadbalancer URL

•              Sample API in vm-app-1 & vm-app-2 should be internally accessible from vm-connect

•              Create a simple AWS RDS/Azure SQL database (project-db) in network-b -> subnet-d

•              The created managed DB should not have egress internet connectivity

•              The sample CRUD API should read/write data to the created managed db

•              Deploy the sample API in serverless resource - AWS Lambda/Azure functions

•              Create 2 S3/Azure blob buckets - 1 publicly accessible and 1 as a private bucket

•              Draw an architecture diagram for the use case using draw.io

 

Sequence Flow

 

•              network-a -> subnet-a -> public -> vm-nginx -> deploy nginx -> should be accessible from user's browser only

•              network-a -> subnet-b -> private -> vm-connect -> deploy nothing

•              network-b -> subnet-c -> private -> vm-app-1 & vm-app-2 -> deploy sample API -> should be publicly accessible via NLB URL -> should be privately accessible from vm-private-1 -> API should connect to RDS DB (project-db) for CRUD operations

•              network-b -> subnet-d -> private -> DB (project-db) -> no egress internet connectivity

•              create a serverless resource and deploy the sample API

•              public storage bucket

•              network-b -> private -> private storage bucket
