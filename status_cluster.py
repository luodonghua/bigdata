#!/usr/bin/python2.7

# Get a handle to the API client
from cm_api.api_client import ApiResource

cm_host = "cdh-vm.dbaglobe.com"
api = ApiResource(cm_host, username="admin", password="admin")

# Get a list of all clusters
cdh5 = None
for c in api.get_all_clusters():
  print str(c)+'\n'
  if c.version == 'CDH5':
    cdh5 = c

if cdh5 <> None:
  print '{}	 {}	{}'.format('Service Name'.ljust(15),'Service State'.ljust(13),'Health Summary')
  print '{}	 {}	{}'.format(('-'*15).ljust(15),('-'*13).ljust(13),('-'*14))
  for s in cdh5.get_all_services():
    print '{}	 {}	{}'.format(s.name.ljust(15),s.serviceState.ljust(13),s.healthSummary)

