#!/bin/bash
for document in $(ls|grep .jemdoc);do jemdoc -c config.conf $document;done
