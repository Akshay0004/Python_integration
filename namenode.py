def namenode():
	import os
	print("\t\t\tAbout namenode:")
	namenode_IP = input("\t\t\tIP at which u going to configure namenode:")
	namenode_folder = input("\t\t\tnamenode folder name:")
	os.system("rm -rf {}".format(namenode_folder))
	os.system("mkdir {}".format(namenode_folder))
	namenode_port = input("\t\t\tPort Number to run namenode service:")
	
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(namenode_folder)
	file_hdfs.write(hdfs_data)





	file_core = open("/etc/hadoop/core-site.xml", "w")
	core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
	file_core.write(core_data)   


	

namenode()
