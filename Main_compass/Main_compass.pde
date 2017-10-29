import processing.io.*;
I2C i2c;
byte mg_register = 0x68;
byte magnetic_register = 0x0C;

int xh,xl,yh,yl,zh,zl;
int x,y,z;

void setup(){
  
  //println("Available I2C interfaces");
  //printArray(I2C.list());
  
  i2c = new I2C(I2C.list()[0]);
  println("Suscess conection to device.");
  
  i2c_write(byte(0x6B),byte(0x00));
  i2c_write(byte(0x6A),byte(0x00));
  i2c_write(byte(0x37),byte(0x02));
  println("Suscess setting initial device main.");
  
  writeMag(byte(0x0A),byte(0x12));
  //i2c.endTransmission();
    
  print("Suscess initial programs.");
}

void draw(){
   background(255);
   
   if (I2C.list() != null)
   {
     //xh = int(readMag(byte(0x04)));
     //xl = int(readMag(byte(0x03)));
     
     //yh = int(readMag(byte(0x06)));
     //yl = int(readMag(byte(0x05)));
     
     //zh = int(readMag(byte(0x08)));
     //zl = int(readMag(byte(0x07)));
     
     //readMag(byte(0x09));
     
     //x = (xh << 8) | (xl & 0xFF);
     //y = (yh << 8) | (yl & 0xFF);
     //z = (zh << 8) | (zl & 0xFF);
   }   
   println("X: " +x+" Y: " +y+ " Z: "+z);
}