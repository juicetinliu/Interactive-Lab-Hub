int yes = 0;
int no = 0;
int total = 0;

int barone = 75;
int bartwo = 125;

void setup(){
  size(250, 300);
}

void draw(){
  background(25);
  //stroke(150,180,255);
  fill(255);
  text("How is everyone feeling today?", 25, 30);
  text("Yes", 50, barone-10);
  text("No", 50, bartwo-10);
  text(yes, 160, barone+5);
  text(no, 160, bartwo+5);
  total = yes+no;
  total = total == 0? 1: total;
  bar(50, barone, 10, 100, float(yes)/float(total), color(150,255,180));
  bar(50, bartwo, 10, 100, float(no)/float(total), color(255,180,180));
}

void bar(float x, float y, float w, float l, float percent, color fillc){
  noStroke();
  
  fill(100);
  ellipse(x, y, w, w);
  ellipse(x+l, y, w, w);
  rect(x, y - w/2, l, w);
  
  fill(fillc);
  ellipse(x, y, w, w);
  ellipse(x+l*percent, y, w, w);
  rect(x, y - w/2, l*percent, w);
}

void keyPressed(){
  if(key == 'y'){
    yes += 1;
  }
  if(key == 'n'){
    no += 1;
  }
  if(key == 't'){
    yes = max(yes - 1, 0);
  }
  if(key == 'b'){
    no = max(no - 1, 0);
  }
  if(key == 'h'){
    yes += 1;
    no = max(no - 1, 0);
  }
  if(key == 'g'){
    no += 1;
    yes = max(yes - 1, 0);
  }
}
