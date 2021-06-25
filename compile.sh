#!/bin/bash
for document in $(ls|grep .jemdoc);do python jemdoc -c config.conf $document;done
