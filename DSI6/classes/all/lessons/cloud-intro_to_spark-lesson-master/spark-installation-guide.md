# Spark Installation Guide

Spark is:

- Distributed computing.
- A framework.
- Machine learning methods.
- Stream processing.

For our future lessons, we'll be exploring the applications of Apache Spark in the big data ecosystem.  


## OS X

For OS X, we'll be using the Brew version of Spark.

## 1.0: Install Hadoop/Java Via Brew

```
brew install hadoop
```
*Hadoop will be installed at path `/usr/local/Cellar/hadoop`.*

> **If Brew complains about Java not being installed:**
> ```
> brew cask install java
> ```
> Then, attempt to install the Hadoop package again.

**If you get "cask command not found:"**
Follow [these directions](https://github.com/caskroom/homebrew-cask/blob/master/doc/reporting_bugs/error_unknown_command_cask.md) to fix your issue, then try again.


## Hadoop Configuration
### 2.0: Configure Hadoop Environment Script

Edit the file: `nano /usr/local/Cellar/hadoop/2.7.3/libexec/etc/hadoop/hadoop-env.sh`.

*Note the version installed, which may be newer than 2.7.3, and update your path accordingly.*

Change the line with `HADOOP_OPTS` from:
```bash
export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true"
```

To:
```bash
export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true -Djava.security.krb5.realm= -Djava.security.krb5.kdc="
```

### 2.1: Configure Hadoop File System (HDFS) Core

Edit the core site configuration file like so:

```bash
nano /usr/local/Cellar/hadoop/2.7.3/libexec/etc/hadoop/core-site.xml
```

Add the following code between the `<configuration></configuration>` tags:

```xml
<property>
<name>hadoop.tmp.dir</name>
<value>/usr/local/Cellar/hadoop/hdfs/tmp</value>
<description>A base for other temporary directories.</description>
</property>
<property>
<name>fs.default.name</name>
<value>hdfs://localhost:9000</value>
</property>
```

These parameters set up the default HDFS storage directory (`/usr/local/Cellar/hadoop/hdfs/tmp`) and site service name (`hdfs://localhost:9000`).

### 2.2: Configure Hadoop

Create a new file called **mapred-site.xml** here:
```bash
nano /usr/local/Cellar/hadoop/2.7.3/libexec/etc/hadoop/mapred-site.xml
```

Paste the following contents into this new file:

```bash
<configuration>
 <property>
  <name>mapred.job.tracker</name>
  <value>localhost:9010</value>
 </property>
</configuration>
```

This sets up the job tracker name that's used to observe jobs in progress.

### 2.3: Configure Hadoop Site HDFS

Edit the following:

```bash
nano /usr/local/Cellar/hadoop/2.7.3/libexec/etc/hadoop/hdfs-site.xml
```

Between the `<configuration></configuration>` tags, add the following:

```bash
 <property>
  <name>dfs.replication</name>
  <value></value>
 </property>
```

*After you’ve added your edits, the actual end of the file should look something like this:*

```xml
<!-- Put site-specific property overrides in this file. -->

<configuration>
 <property>
  <name>dfs.replication</name>
  <value></value>
 </property>
</configuration>
```

### 2.4: Configure Hadoop Startup Scripts

If you are using a Bash shell (which is the default), you should add these lines to your Bash profile file `~/.bash_profile`:

```bash
alias hstart="/usr/local/Cellar/hadoop/2.7.3/sbin/start-dfs.sh;/usr/local/Cellar/hadoop/2.7.3/sbin/start-yarn.sh"
alias hstop="/usr/local/Cellar/hadoop/2.7.3/sbin/stop-yarn.sh;/usr/local/Cellar/hadoop/2.7.3/sbin/stop-dfs.sh"
```

Then, reload your Bash profile by typing:

```bash
source ~/.bash_profile
```

### 2.5 - Format/Init Hadoop HDFS

If you set everything up correctly, the following command will format your default HDFS system:

```bash
hdfs namenode -format
```

Also, if you want to get rid of your current HDFS system and start fresh, you can always rerun this command.


### 2.6: Check That the SSH Key is Set Up

In order for your localhost to accept incoming connections through the HDFS service, we need to make sure SSH is set up with the proper keys. These will likely be set up already. You can check by typing:

`ssh-keygen -t rsa`

If the keygen script asks you to overwrite your existing keys, there's no need to do so. Abort the script by hitting **Ctrl-C**.

*Note the prompt to "Overwrite (y/n)?". Hit Ctrl-C in this case. If that prompt doesn’t pop up, just keep hitting enter, accepting all defaults *without* typing any passwords.*
```
(auto) Davids-MacBook-Pro-3:random_forest_run davidyerrington$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/davidyerrington/.ssh/id_rsa):
/Users/davidyerrington/.ssh/id_rsa already exists.
Overwrite (y/n)?
```

Additionally, **enable Remote Login** by navigating to System Preferences -> Sharing.
- Check “Remote Login.”

![](https://snag.gy/w4QTKm.jpg)

**Authorize SSH Keys**
<br>
**ONLY DO THIS IF YOU DIDN'T HAVE THE id_rsa FILE IN THE PRIOR STEP.**

To allow your system to accept the login, we have to make it aware of the keys that will be used:
```cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys```

You should be able to log in remotely. Test this by typing:

```
ssh localhost
```

### 2.7: Start Hadoop

```
hstart
```

Once you start the HDFS daemon, you may be prompted multiple times for sudo access for the startup script. Enter your user password to allow these operations.

Also, whenever you want to stop this service, you can type `hstop`. Know that this sometimes takes a while. You may also be prompted for passwords, which is OK.

### 2.8: Get Some Coffee

Congratulations — you're done configuring Hadoop! Hadoop has an intense configuration prerequisite. If you'd like, take a break. You deserve it.

## ~~3.0: Install Spark via Brew~~

```
~~brew install apache-spark~~
```

> installs Spark to directory /usr/local/Cellar/apache-spark/2.*

~~Add this to your ~/.bash_profile~~
```
alias jupyter-spark='PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS="notebook" pyspark'
export SPARK_HOME='/usr/local/Cellar/apache-spark/2.0.0/libexec/'
```

~~Then, reload your `bash_profile`:~~

```
source ~/.bash_profile
```

~~Then, run Jupyter Notebook again using `jupyter-spark`, which is the alias you just created! Check in a new notebook that the "sc" variable exists.~~

## 3.0: Manually Install Spark

*Please read **all** of the instructions before you begin. There are some important details and options available.*

> First and foremost, remove the Brew version of Spark if you've installed it on OS X:

> `brew uninstall apache-spark`

To install/configure Apache Spark, we'll do the following:

1) Navigate to the Apache Spark download page.
2) Download the latest version to `/usr/local/`.
3) Unarchive Spark.
4) Set an environment variable called `SPARK_HOME` in your `.bash_profile`, which other applications on your system will use to determine where Spark is installed. We put it in `.bash_profile` because we want the environment variable to persist to every terminal session we use in the future.

### 1+2. Download the Latest Version of Spark

Take note of the version that you downloaded (use the pre-built for Hadoop version):
http://spark.apache.org/downloads.html.

Download your version to your `/usr/local` directory. You can click the download link and move the file, you can copy the download link, **or**, you can use `wget` while you are in `/usr/local` from the terminal/Bash to download the latest version.

![](https://snag.gy/MAvKIH.jpg)
_The download link is listed here as number four._

*Alternatively, you can download with `wget`.*
_The actual version and link may differ from what's listed in the example below. If the link is broken by the time you're reading this, go to the Apache Spark Downloads page and get an updated link/version of Spark from there._
```
cd /usr/local
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
```

### 3. Unarchive Apache Spark
The file you downloaded is compressed, so you'll need to unarchive and decompress it. Use the following command with respect to your file. If the file/version has updated, please adjust for your version.

```
tar -xzvf spark-2.1.0-bin-hadoop2.7.tgz # Or, the file name corresponding to the one you downloaded.
```
_You should have this file in `/usr/local` if you followed Step 1. If not, return to the beginning and double-check._

This command should expand Spark into `/usr/local/spark-2.1.0-bin-hadoop2.7`. If you downloaded a newer version, this directory will reflect that.

To make our lives easier in the future, we are going to “symbolically link” our Spark directory to one called `/usr/local/spark`. In the future, we might want to download and install a newer version of Spark or use different versions of Spark without having to refer to a complicated-looking directory like `/usr/local/spark-2.1.0-bin-hadoop2.7`. This will allow us to do that. We can reference `/usr/local/spark`, and, while it's symbolically linked to `/usr/local/spark-2.1.0-bin-hadoop2.7` — or perhaps a future version like `/usr/local/spark-2.1.1345-bin-hadoop2.7` — we only need to update the symbolic link.


*Symlink Spark*
Now, we only need to refer to Spark as `/usr/local/spark`.
`ln -s /usr/local/spark-2.1.0-bin-hadoop2.7 /usr/local/spark`

### 4. Configure Environmental Variable

Now that we have our symbolic link to `/usr/local/spark`, we need to set the `SPARK_HOME` environmental variable to point to it, as well as add `/usr/local/spark/bin` to our system's $PATH variable so we can type "pyspark" from anywhere and it will run.

**Edit your `~/.bash_profile`:**

`nano ~/.bash_profile`

**Add these lines to the end of your `.bash_profile`:**

```
SPARK_HOME="/usr/local/spark"
PATH="/usr/local/spark/bin:$PATH"
```

**Update your environment with these settings:**

```
source ~/.bash_profile
```
