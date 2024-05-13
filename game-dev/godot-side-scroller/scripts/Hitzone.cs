using Godot;
using System;

public partial class Hitzone : Area2D
{	
	// property to specify the damage amount for this Hitzone
	[Export]
	public int DamageAmount { get; set; } = 10;
	
	private Player player;
	
	public override void _Ready()
	{
		Connect("body_entered", new Callable(this, nameof(OnBodyEntered)));
		
		player = GetNode<Player>("/root/Game/Player");
		if (player == null)
		{
			GD.Print("Player not found.");
		}
	}
	
	public override void _Process(double delta)
	{
	}

	private void OnBodyEntered(Node2D body)
	{
		if (body is Player)
		{
			player.ReduceHealth(DamageAmount);
		}
	}
}
