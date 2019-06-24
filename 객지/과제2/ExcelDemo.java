package project2;
import javax.swing.table.*;
import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.StringTokenizer;

public class ExcelDemo extends JFrame{
   private JScrollPane scrollPane;
   private JTable table, headerTable;
   private JMenuBar menuBar;
   private JMenu fileMenu, formulasMenu, functionMenu;
   private JMenuItem newItem, open, save, exit, sum, average, count, max, min;
   private String title;
   private int cardinality, degree;

   public static void main(String args[]) {
      new ExcelDemo();
   }
   
   public ExcelDemo(){
      //********** Main Table Setting ************//
      String[][] data = new String[100][26];
      String[] dataColumn = new String[26];   
      char ch = 'A';
      for(int i = 0; i< 26; i++, ch++) {
         dataColumn[i] = Character.toString(ch);
      }
      DefaultTableModel model = new DefaultTableModel(data, dataColumn);
      table = new JTable(model);   
      table.setCellSelectionEnabled(true);
      table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
      
      //********** Header Table Setting ************//
      DefaultTableModel headerModel = new DefaultTableModel() {
            @Override
            public int getColumnCount() {
                return 1;
            }         
            @Override
            public boolean isCellEditable(int row, int col) {
                return false;
            }
            @Override
            public int getRowCount() {
                return table.getRowCount();
            }
      };
      headerTable = new JTable(headerModel);
      for (int i = 0; i < table.getRowCount(); i++) {
            headerTable.setValueAt("" + i, i, 0);
        }
        headerTable.setPreferredScrollableViewportSize(new Dimension(50, 0));
        headerTable.getColumnModel().getColumn(0).setCellRenderer(new TableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(JTable x, Object value, boolean isSelected, boolean hasFocus, int row, int column) {
                Component component = table.getTableHeader().getDefaultRenderer().getTableCellRendererComponent(table, value, false, false, -1, -2);
                return component;
            }
        });

      //********** Scroll Setting ************//
      scrollPane = new JScrollPane(table);
      scrollPane.setRowHeaderView(headerTable);      
      add(scrollPane);
      
      //********** Etc Setting ************//
      title = "새 Microsoft Excel 워크시트.xlsx - Excel"; 
      setTitle(title);
      setSize(610, 588);
      createMenu();
      setLocationRelativeTo(null);
      createMenu();
      setVisible(true);
       setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);     
   }
   
   public void createMenu() {
      //File Menu: New, Open, Save, Exit
      //Formulas Menu: Function(SUM, AVERAGE, COUNT, MAX, MIN)      
      menuBar = new JMenuBar();
      fileMenu = new JMenu("File");
      formulasMenu = new JMenu("Formulas");
      functionMenu = new JMenu("Funtion");
      
      //********** FileMenu Setting ************//
      newItem = new JMenuItem("New");     
      open = new JMenuItem("Open");
      save = new JMenuItem("Save");
      exit = new JMenuItem("Exit");
      fileMenu.add(newItem);
      fileMenu.add(open);
      fileMenu.addSeparator();
      fileMenu.add(save);
      fileMenu.addSeparator();
      fileMenu.add(exit);

      //********** Function Menu Setting ************//
      sum = new JMenuItem("SUM");
      average = new JMenuItem("AVERAGE");
      count = new JMenuItem("COUNT");
      max = new JMenuItem("MAX");
      min = new JMenuItem("MIN");
      functionMenu.add(sum);
      functionMenu.add(average);
      functionMenu.add(count);
      functionMenu.add(max);
      functionMenu.add(min);

      //********** Formulas Menu Setting ************//
      formulasMenu.add(functionMenu);

      //********** MenuBar Setting ************//
      menuBar.add(fileMenu);
      menuBar.add(formulasMenu);
      setJMenuBar(menuBar);
      
      //********** newItem, open, save, exit ************//
      newItem.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            new ExcelDemo();
            dispose();            
         }               
      });
      
      open.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            //선택한 파일 경로 불러오기
            JFileChooser chooser = new JFileChooser(); 
            chooser.setFileFilter(new FileNameExtensionFilter("텍스트문서(*.txt, *.csv)", "csv", "txt"));
            int fileOpen = chooser.showOpenDialog(null);  
            if (fileOpen != JFileChooser.APPROVE_OPTION) {
               return;
            }
            String filePath = chooser.getSelectedFile().getPath(); 
            
            try {
               FileReader fr = new FileReader(filePath);
               BufferedReader br = new BufferedReader(fr);      
               //기존에 있던 값 초기화
               DefaultTableModel model = (DefaultTableModel)table.getModel();
               for(int i = 0; i < 101; i++) {
                  model.setNumRows(i);
               }
               //파일 읽어오기
               for(int i = 0; i < 100; i++) {
                  String str = br.readLine();                  
                  if(str != null) {
                     if(str.contains(",")) {
                        StringTokenizer st = new StringTokenizer(str, ",", true);
                        //구분자까지 토큰에 포함시킨다
                        //if(토큰 == ",") -> token == null So, col값인 j를 ++한다.  
                        //마지막 col은 구분자가 없기 때문에 예외처리를 해준다
                        for(int j = 0; j < 26;) {
                           if(st.hasMoreTokens()) {
                              String token = st.nextToken();
                              if(token.contentEquals(",")) {
                                 j++;
                              }else{
                                 table.setValueAt(token, i, j);
                                 System.out.println(token);
                              }
                           }else {
                              j++;
                           }
                        }
                     }else {
                        table.setValueAt(str, i, 0);
                        System.out.println(str);
                     }
                  }else {
                     //정보가 없는 파일일 경우에 null로 전부 초기화 해야하는데, 미리 초기화 했기 때문에 구현X
                  }
               }
               setTitle(filePath);            
               br.close();
            } catch (FileNotFoundException e1) {
               e1.printStackTrace();            
            } catch (IOException e1) {
               e1.printStackTrace();
            }
         }
      });
      save.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            //선택한 경로에 파일 저장
            String filePath;
            JFileChooser chooser = new JFileChooser();   
            chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY); 
         
            int re = chooser.showSaveDialog(null);
            if (re == JFileChooser.APPROVE_OPTION) {
               filePath = chooser.getSelectedFile().getPath(); 
               System.out.println(filePath);
            }else{
               return;
            }
            
            try {
               FileWriter fw = new FileWriter(filePath);
               BufferedWriter bw = new BufferedWriter(fw);
               for(int i = 0; i < 100; i++) {
                  String str = "";
                  for(int j = 0; j < 26; j++) {
                     if(table.getValueAt(i, j) != null) {
                        str += table.getValueAt(i, j);
                     }
                     if(j != 25) {
                        str += ",";
                     }
                  }
                  str += "\n";
                  bw.write(str);
               }
               bw.close();
            } catch (IOException e1) {
               e1.printStackTrace();
            }
            
         }
      });
      exit.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            System.exit(0);
         }
      });

      //********** Save ClikedMouse Position ************//
      table.addMouseListener(new MouseAdapter() {
         @Override
         public void mouseClicked(MouseEvent e) {
            table = (JTable)e.getComponent();
            cardinality = table.getSelectedRow();
            degree = table.getSelectedColumn();
         }
      });
      
      //********** sum, average, max, min ************//
      sum.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            String input = JOptionPane.showInputDialog(null,"Function Arguments", "SUM",-1);
            if(input == null) {
               return;
            }
            StringTokenizer st = new StringTokenizer(input, ":");
            String startPoint = st.nextToken();
            String finalPoint = st.nextToken();
            int colStartPoint = startPoint.charAt(0) - 'A';
            int colFinalPoint = finalPoint.charAt(0) - 'A';
            int rowStartPoint = Integer.parseInt(startPoint.substring(1, startPoint.length()));
            int rowFinalPoint = Integer.parseInt(finalPoint.substring(1, finalPoint.length()));
            
            double sum = 0;
            for(int i = rowStartPoint; i <= rowFinalPoint; i++) {
               for(int j = colStartPoint; j <= colFinalPoint; j++) {
                  if(table.getValueAt(i, j) != null) {
                     double value = Double.parseDouble(table.getValueAt(i, j).toString());
                     sum += value;            
                  }
               }
            }   
            table.setValueAt((Object)sum, cardinality, degree);
         }
      });
      average.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            String input = JOptionPane.showInputDialog(null,"Function Arguments", "Average",-1);   
            if(input == null) {
               return;
            }
            StringTokenizer st = new StringTokenizer(input, ":");
            String startPoint = st.nextToken();
            String finalPoint = st.nextToken();
            int colStartPoint = startPoint.charAt(0) - 'A';
            int colFinalPoint = finalPoint.charAt(0) - 'A';
            int rowStartPoint = Integer.parseInt(startPoint.substring(1, startPoint.length()));
            int rowFinalPoint = Integer.parseInt(finalPoint.substring(1, finalPoint.length()));
            
            double average = 0, sum = 0;
            int cnt = 0;
            for(int i = rowStartPoint; i <= rowFinalPoint; i++) {
               for(int j = colStartPoint; j <= colFinalPoint; j++) {
                  if(table.getValueAt(i, j) != null) {
                     double value = Double.parseDouble(table.getValueAt(i, j).toString());
                     sum += value;
                     cnt++;
                  }
               }
            }      
            average = sum / cnt;
            table.setValueAt((Object)average, cardinality, degree);
            
         }
      });
      
      count.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            String input = JOptionPane.showInputDialog(null,"Function Arguments", "Count",-1);
            if(input == null) {
               return;
            }
            StringTokenizer st = new StringTokenizer(input, ":");
            String startPoint = st.nextToken();
            String finalPoint = st.nextToken();
            int colStartPoint = startPoint.charAt(0) - 'A';
            int colFinalPoint = finalPoint.charAt(0) - 'A';
            int rowStartPoint = Integer.parseInt(startPoint.substring(1, startPoint.length()));
            int rowFinalPoint = Integer.parseInt(finalPoint.substring(1, finalPoint.length()));
            System.out.println(colStartPoint + " " + colFinalPoint + " " + rowStartPoint + " " + rowFinalPoint);
            
            int cnt = 0;
            for(int i = rowStartPoint; i <= rowFinalPoint; i++) {
               for(int j = colStartPoint; j <= colFinalPoint; j++) {
                  if(table.getValueAt(i, j) != null) {
                     cnt++;
                  }
               }
            }      
            table.setValueAt((Object)cnt, cardinality, degree);
            
         }
      });
      max.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            String input = JOptionPane.showInputDialog(null,"Function Arguments", "Max",-1);
            if(input == null) {
               return;
            }
            StringTokenizer st = new StringTokenizer(input, ":");
            String startPoint = st.nextToken();
            String finalPoint = st.nextToken();
            int colStartPoint = startPoint.charAt(0) - 'A';
            int colFinalPoint = finalPoint.charAt(0) - 'A';
            int rowStartPoint = Integer.parseInt(startPoint.substring(1, startPoint.length()));
            int rowFinalPoint = Integer.parseInt(finalPoint.substring(1, finalPoint.length()));
            
            double max = Double.MIN_VALUE;
            for(int i = rowStartPoint; i <= rowFinalPoint; i++) {
               for(int j = colStartPoint; j <= colFinalPoint; j++) {
                  if(table.getValueAt(i, j) != null) {
                     double value = Double.parseDouble(table.getValueAt(i, j).toString());
                     if(max < value) {
                        max = value;
                     }
                  }
               }
            }      
            table.setValueAt((Object)max, cardinality, degree);
            
         }
      });
      min.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            String input = JOptionPane.showInputDialog(null,"Function Arguments", "Min",-1);   
            if(input == null) {
               return;
            }
            StringTokenizer st = new StringTokenizer(input, ":");
            String startPoint = st.nextToken();
            String finalPoint = st.nextToken();
            int colStartPoint = startPoint.charAt(0) - 'A';
            int colFinalPoint = finalPoint.charAt(0) - 'A';
            int rowStartPoint = Integer.parseInt(startPoint.substring(1, startPoint.length()));
            int rowFinalPoint = Integer.parseInt(finalPoint.substring(1, finalPoint.length()));
            
            double min = Double.MAX_VALUE;
            for(int i = rowStartPoint; i <= rowFinalPoint; i++) {
               for(int j = colStartPoint; j <= colFinalPoint; j++) {
                  if(table.getValueAt(i, j) != null) {
                     double value = Double.parseDouble(table.getValueAt(i, j).toString());
                     if(min > value) {
                        min = value;
                     }
                  }
               }
            }      
            table.setValueAt((Object)min, cardinality, degree);
         }
      });
   }
}
