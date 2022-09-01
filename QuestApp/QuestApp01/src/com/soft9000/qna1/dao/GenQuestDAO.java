/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.soft9000.qna1.dao;

import com.soft9000.SQLMate.EColumnType;
import com.soft9000.SQLMate.ExInvalid;
import com.soft9000.SQLMate.SourceCodeFormatter;
import com.soft9000.SQLMate.SqlCodeJavaJdbc;
import com.soft9000.SQLMate.SqlColumn;

/**
 *
 * @author profnagy
 */
public class GenQuestDAO {

    public static void main(String... args) throws ExInvalid {
        SqlCodeJavaJdbc test = new SqlCodeJavaJdbc();
        test.getTable().setTableName("Questions");
        test.getTable().getColumns().add(new SqlColumn("ID", EColumnType.Integer));
        test.getTable().getColumns().add(new SqlColumn("KID", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("GID", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("Question", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("Answer", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("Difficulty", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("Association", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("Status", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("Language", EColumnType.Text));
        test.getTable().getColumns().add(new SqlColumn("Code1", EColumnType.Integer));
        test.getTable().getColumns().add(new SqlColumn("Code2", EColumnType.Integer));
        test.getTable().getColumns().add(new SqlColumn("Version", EColumnType.Real));
        test.getConn().setDbFileName("QuestDAO");
        test.getConn().setDbFilePath("com/soft9000");
        StringBuilder sb = new StringBuilder();
        test.write(sb);

        // Still a tad ugly - needs some work - feel free to omit / manually format output in your IDE;
        System.out.println(SourceCodeFormatter.FormatCode(sb.toString()));
    }
}
