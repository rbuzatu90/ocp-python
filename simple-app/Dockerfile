# We are basing our builder image on openshift base-centos7 image
FROM openshift/base-centos7

# Inform about software versions being used inside the builder
ENV app=lol

#RUN yum install -y lighttpd && \
    # clean yum cache files, as they are not needed and will only make the image bigger in the end
#    yum clean all -y
#RUN yum install -y httpd
# Copy the S2I scripts to /usr/libexec/s2i which is the location set for scripts
# in openshift/base-centos7 as io.openshift.s2i.scripts-url label
COPY ./s2i/bin/ /usr/libexec/s2i

# Copy the lighttpd configuration file
COPY ./myapp.py /opt/app-root/src/
# Drop the root user and make the content of /opt/openshift owned by user 1001
RUN chown -R 1001:1001 /opt/app-root
RUN touch /opt/app-root/lol
RUN yum install -y python-setuptools tcpdump iproute net-tools
RUN easy_install pip
RUN pip install gunicorn
RUN pip install flask
# Set the default user for the image, the user itself was created in the base image
USER 1001

# Specify the ports the final image will expose

# Set the default CMD to print the usage of the image, if somebody does docker run
CMD ["/usr/libexec/s2i/run"]
