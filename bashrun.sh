#!/bin/sh
for i in {0..10}
do
  name="dummy$i.py"
  nohup python3 $name &
done
