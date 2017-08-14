import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JPanel;

public class GamePanel extends JPanel{
    private FrameRate frameRate;
    
    public GamePanel (FrameRate frameRate) {
        this.frameRate = frameRate;
    }
    
    public void paint(Graphics g) {
        super.paint(g);
        onPaint(g);
    }
    
    protected void onPaint(Graphics g) {
        frameRate.calculate();
        g.setColor(Color.WHITE);
        g.drawString(frameRate.getFrameRate(), 30, 30);
        repaint();
    }

}