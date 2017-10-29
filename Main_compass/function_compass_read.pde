byte read(byte address)
{
    i2c.beginTransmission(mg_register);
    i2c.write(address);
    i2c.endTransmission();
    
    i2c.beginTransmission(mg_register);
    byte[] val = i2c.read(1);
    i2c.endTransmission();
    return val[0];
}

void write(byte address, byte data)
{
    i2c.beginTransmission(mg_register);
    i2c.write(address);
    i2c.write(data);
    //i2c.endTransmission();
}

byte readMag(byte reg)
{
     i2c.beginTransmission(magnetic_register);
     i2c.write(reg);
     //i2c.endTransmission();
     
     i2c.beginTransmission(magnetic_register);
     byte[] val = i2c.read(1);
     i2c.endTransmission();
     return val[0];
}


void writeMag(byte address, byte data)
{
      i2c.beginTransmission(magnetic_register);
      i2c.write(address);
      i2c.write(data);
      //i2c.endTransmission();
}